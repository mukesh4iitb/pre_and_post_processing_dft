#!/bin/bash

# Extension of ls command:
ls_list(){
echo "[" $(ls -d "$@" | awk '{print "`" $1 "`"}' | sed 's/`/"/g' | paste -sd ",") "]"
}



ls_array(){
echo "(" $(ls -d "$@" | awk '{print "`" $1 "`"}' | sed 's/`/"/g' | paste -sd " ") ")"
}


find_array() {
    local search_path="${1}"   # default: current directory
    local pattern="${2}"   # default: pattern
    local array_var="${3:-dirs}"  # default Bash array name

    # Use indirect reference to assign the array
    mapfile -t tmp_array < <(find "$search_path" -type d -name "$pattern")
    echo ${tmp_array[@]}
    eval "$array_var=(\"\${tmp_array[@]}\")"
}



find_list() {
    local search_path="${1}"
    local pattern="${2}"
    local py_var="${3:-dirs}"  # Python variable name

    # Read find output and convert to Python list literal
    local py_list
    py_list=$(find "$search_path" -type d -name "$pattern" -print0 | \
              xargs -0 -I{} printf '%q\n' "{}" | \
              python3 -c "import sys; print(list(map(str.strip, sys.stdin)))")

    # Export as shell variable
    echo $py_list

    eval "$py_var=\"$py_list\""
}



## cd to scratch directory

scd() {
    #echo "slurm-output:"
    #cat *.o*

    scratch_path=$(sed -n '/SCRATCH DIR:/p' *.o* | awk '{print $3}')
    echo "Scratch path: $scratch_path"

    if [ -d "$scratch_path" ]; then
        cd "$scratch_path"
    else
        echo "Error: Scratch path is invalid or does not exist."
    fi
}

# from scratch to submitting directory
sucd() {
    #echo "slurm-output:"
    #cat *.o*

    submit_path=$(sed -n '/SUBMIT DIR:/p' *.o* | awk '{print $3}')
    echo "Submit dir path: $submit_path"

    if [ -d "$submit_path" ]; then
        cd "$submit_path"
    else
        echo "Error: Submit path is invalid or does not exist."
    fi
}


# copying job scripts
cjob() {
    cp /<path of job-script>/job.sh "$1"
}
