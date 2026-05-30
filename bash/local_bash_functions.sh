#!/usr/bin/bash


conv_plot(){
	echo "List of all available functions:"
""	
}

venergy_convergence_by_jobid(){
    jobid=$1

    # Get the working directory of the job
    workdir=$(ssh cmu_rsync "scontrol show job $jobid" | grep 'WorkDir' | awk -F '=' '{print $2}')
    echo "Working directory: $workdir"

    # Check if the directory was found
    if [ -z "$workdir" ]; then
        echo "Not found working directory for job ID: $jobid"
        return 1
    fi

    # Define a unique output file for each job
    energy_file="Energy_${jobid}.dat"
    
    if [ -f $energy_file ]; then
        rm $energy_file
    fi

    # Extract energies from vasp.out
    ssh cmu_rsync "grep 'F=' $workdir/vasp.out" | awk '{print $5}' > $energy_file

    # Run Python script
    python3 ~/Energy_convergence.py "$energy_file"
}


#venergy_convergence_by_jobid 53844067

lvenergy_convergence_by_jobid(){
    for jobid in "$@"; do
        echo "Processing Job ID: $jobid"

        # Get the working directory of the job
        workdir=$(ssh cmu_rsync "scontrol show job $jobid" | grep 'WorkDir' | awk -F '=' '{print $2}')
        echo "Working directory: $workdir"

        # Check if the directory was found
        if [ -z "$workdir" ]; then
            echo "Not found working directory for job ID: $jobid"
            continue
        fi

        # Define a unique output file for each job
        energy_file="Energy_${jobid}.dat"
    
	if [ -f $energy_file ]; then
            rm $energy_file
        fi

        # Extract energies from vasp.out
        ssh cmu_rsync "grep 'F=' $workdir/vasp.out" | awk '{print $5}' > "$energy_file"

        echo "Saved energy data to $energy_file"

        # Optionally run your Python script on this file
        python3 ~/Energy_convergence.py "$energy_file"
    done
}

neb_plot(){
python3  ~/codes/mycodes/neb_plot.py "$@"
}

neb_barrier_plot_pq(){
python3  ~/codes/mycodes/neb_barrier_plot_pq.py "$@"
}
neb_spline_plot_pq(){
python3  ~/codes/mycodes/neb_spline_plot_pq.py "$@"
}


# cleaning the bib file and generating one with only citation in tex file.
getcleanbib() {
    if [[ -z "$1" ]]; then
        echo "Usage: bibclean <tex-filename-without-extension>"
        return 1
    fi

    local base="$1"
    local tmpbib="${base}_cited_tmp.bib"
    local outbib="${base}_references.bib"

    # Step 1: extract cited references
    if [[ -f "${base}.bcf" ]]; then
        echo "Detected biber workflow (.bcf)"
        biber --output_format=bibtex \
              --output_resolve \
              --output-file "$tmpbib" \
              "$base"

    elif [[ -f "${base}.aux" ]]; then
        echo "Detected BibTeX workflow (.aux)"
        bibexport -o "$tmpbib" "${base}.aux"

    else
        echo "Error: No .aux or .bcf file found"
        return 1
    fi

    # Step 2: clean unwanted fields using Python
    python3 <<EOF
import bibtexparser

with open("$tmpbib") as bibfile:
    bib_database = bibtexparser.load(bibfile)

for entry in bib_database.entries:
    entry.pop("abstract", None)

with open("$outbib", "w") as bibfile:
    bibtexparser.dump(bib_database, bibfile)

EOF

    rm -f "$tmpbib"
    echo "✔ Clean bibliography written to $outbib"
}
#gencleanbib main


vasp2cif () {
  if [ "$#" -eq 0 ]; then
    echo "Usage: vasp2cif file1 [file2 ...]"
    return 1
  fi

  for input in "$@"; do
    ase convert -i vasp "$input" -o cif "${input%.*}.cif"
  done
}
