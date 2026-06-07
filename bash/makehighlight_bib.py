import re
import bibtexparser
import bibtexparser.middlewares as m

def highlight_reference(db, citation_key, color="blue"):

    fields_to_highlight = {
        "title",
        "author",
        "journal",
        "volume",
        "pages"
    }

    for entry in db.entries:
        if entry.get("ID") == citation_key:

            for field in fields_to_highlight:
                if field in entry:
                    entry[field] = (
                        rf"\textcolor{{{color}}}{{{entry[field]}}}"
                    )

            return True

    return False


def highlight_author_in_bib(
    input_file,
    output_file,
    first_name="Mukesh",
    last_name="Singh",
    style="bold",   # options: "bold", "color"
    color="blue"
):
    """
    Highlights a specific author name in a BibTeX file.

    Parameters:
        input_file (str): Path to input .bib file
        output_file (str): Path to output .bib file
        first_name (str): First name to match
        last_name (str): Last name to match
        style (str): "bold" or "color"
        color (str): color name if style="color"
    """

    # Read input
    with open(input_file) as f:
        bibtex_str = f.read()

    # Parse
    library = bibtexparser.parse_string(
        bibtex_str,
        append_middleware=[
            m.SeparateCoAuthors(True),
            m.SplitNameParts(True),
        ],
    )

    # Highlight
    for entry in library.entries:
        for field in entry.fields:
            if field.key == "author":
                for author in field.value:
                    first = " ".join(author.first)
                    last = " ".join(author.last)

                    if first == first_name and last == last_name:
                        if style == "bold":
                            author.first = [rf"\textbf{{{first_name}}}"]
                            author.last = [rf"\textbf{{{last_name}}}"]

                        elif style == "color":
                            author.first = [rf"\textcolor{{{color}}}{{{first_name}}}"]
                            author.last = [rf"\textcolor{{{color}}}{{{last_name}}}"]

    # Write output
    output = bibtexparser.write_string(
        library,
        prepend_middleware=[
            m.MergeNameParts("first"),
            m.MergeCoAuthors(True),
        ],
    )

    with open(output_file, "w") as f:
        f.write(output)


# highlight_author_in_bib("input.bib", "output.bib", style='bold')



def find_added_refs(diff_bbl_path):
    # Step 1: Parse the diff.bbl file to find keys of added references
    with open(diff_bbl_path, 'r', encoding='utf-8') as f:
        bbl_content = f.read()

    # Find all content trapped between \DIFaddbegin and \DIFaddend
    added_blocks = re.findall(r'\\DIFaddbegin(.*?)\\DIFaddend', bbl_content, re.DOTALL)
    
    added_keys = set()
    for block in added_blocks:
        keys = re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}', block)
        for key in keys:
            added_keys.add(key.strip())

    print(f"Found {len(added_keys)} newly added references in the .bbl file.")
    print(added_keys)
    return added_keys


with open("main_references.bib", encoding="utf-8") as f:
    db = bibtexparser.load(f)

keys_to_highlight = find_added_refs(diff_bbl_path='diff.bbl')

for key in keys_to_highlight:
    found = highlight_reference(db, key)

    if not found:
        print(f"Warning: '{key}' not found")

with open("highlighted_reference.bib", "w", encoding="utf-8") as f:
    bibtexparser.dump(db, f)
