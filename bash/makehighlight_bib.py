import re
import bibtexparser

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
