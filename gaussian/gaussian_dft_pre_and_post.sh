xyz2gjf() {
    input="$1"
    output="$2"

    if [[ ! -f "$input" ]]; then
        echo "Error: Input file '$input' not found."
        return 1
    fi

    # Read from line 3 to end
    line3_onwards=$(tail -n +3 "$input")

    # Write to output file
    {
        echo "#B3LYP/6-31+G(d) OPT FREQ"
        echo
        echo "Energy MS-generated"
        echo
        echo "0 1"
        echo "$line3_onwards"
        echo
    } > "$output"

    echo "Generated $output from $input"
}

#xyz2gjf example_01_molecule.xyz example_01_molecule.gjf


xyz2_inp() {
    input="$1"
    output="$2"
    func="$3"
    basis="$4"
    name="${5:-default}"

    if [[ ! -f "$input" ]]; then
        echo "Error: Input file '$input' not found."
        return 1
    fi

    # Read from line 3 to end
    line3_onwards=$(tail -n +3 "$input")
    
    
    # Write to output file
    {
        echo "#B3LYP/6-311+G** OPT FREQ"
        echo
        echo "$name"
        echo
        echo "0 1"
        echo "$line3_onwards"
        echo
    } > "$output"
    
    sed -i "1i\\
%nprocshared=32\\
%mem=8GB\\
%chk=$name.chk" "$output"
    sed -i "/OPT/c\\
#p $func/$basis\\
opt freq\\
scf=(novaracc, tight)\\
int(grid=ultrafine)" "$output"
    
    echo "Saved to $output"
}

#xyz2_inp example_02_molecule.xyz example_02_molecule_pbe.com PBEPBE 6-311+G**
#xyz2_inp example_02_molecule.xyz example_02_molecule_hse.com HSEh1PBE 6-311+G**



xyz2_gen_inp() {
    input="$1"
    output="$2"
    func="$3"
    basis_path="$4"
    name="${5:-default}"

    if [[ ! -f "$input" ]]; then
        echo "Error: Input file '$input' not found."
        return 1
    fi

    # Read from line 3 to end
    line3_onwards=$(tail -n +3 "$input")
    
    
    # Write to output file
    {
        echo "#$func/gen OPT FREQ"
        echo
        echo "$name"
        echo
        echo "0 1"
        echo "$line3_onwards"
        echo
	echo "@$basis_path"
	echo 
    } > "$output"
    
    sed -i "1i\\
%nprocshared=8\\
%mem=8GB\\
%chk=$name.chk" "$output"
    
    echo "Saved to $output"
}

#basis_path="/mnt/home/k0122399/gauss/def2-QZVPD.bas"
#xyz2_gen_inp example_03_molecule.xyz example_03_molecule_pbe.com PBEPBE $basis_path
#xyz2_gen_inp example_03_molecule.xyz example_03_molecule_hse.com HSEh1PBE $basis_path

#------------------------------------------------------------------------------------------------


# some specific basis set and functional used regularly has input generator functions such 
# 1- xyz2_b3lyp_inp: it generate input with b3lyp functional and 6-311G** basis set. 
# 2- xyz2_pbe_inp: it generate input with pbe functional and 6-311G** basis set.
# 3- xyz2_hse_inp: it generate input with hse functional and 6-311G** basis set.
# 4- xyz2_lad_inp: it generate input with lda functional and 6-311G** basis set.


xyz2_b3lyp_inp() {
    input="$1"
    output="$2"
    name="${3:-default}"

    if [[ ! -f "$input" ]]; then
        echo "Error: Input file '$input' not found."
        return 1
    fi  

    # Read from line 3 to end
    line3_onwards=$(tail -n +3 "$input")
    
    
    # Write to output file
    {   
        echo "#B3LYP/6-311+G** OPT FREQ"
        echo
        echo "$name"
        echo
        echo "0 1"
        echo "$line3_onwards"
        echo
    } > "$output"
    
    sed -i "1i\\
%nprocshared=32\\
%mem=8GB\\
%chk=Name.chk" "$output"
    
    echo "Saved to $output"
}


#xyz2_b3lyp_inp example_04_molecule.xyz example_04_molecule_b3lyp.com 

xyz2_hse_inp() {
    input="$1"
    output="$2"
    name="${3:-default}"

    if [[ ! -f "$input" ]]; then
        echo "Error: Input file '$input' not found."
        return 1
    fi  

    # Read from line 3 to end
    line3_onwards=$(tail -n +3 "$input")
    
    
    # Write to output file
    {   
        echo "#B3LYP/6-31+G(d) OPT FREQ"
        echo
        echo "$name"
        echo
        echo "0 1"
        echo "$line3_onwards"
        echo
    } > "$output"
    
    sed -i "1i\\
%nprocshared=32\\
%mem=8GB\\
%chk=$name.chk" "$output"
    
    sed -i "/OPT/c\\
#p HSEh1PBE/6-311+G**\\
opt freq\\
scf=(novaracc, tight)\\
int(grid=ultrafine)" "$output"
    
    echo "Saved to $output"
}


#xyz2_hse_inp example_05_molecule.xyz example_05_molecule_hse.com 

xyz2_pbe_inp() {
    input="$1"
    output="$2"
    name="${3:-default}"

    if [[ ! -f "$input" ]]; then
        echo "Error: Input file '$input' not found."
        return 1
    fi  

    # Read from line 3 to end
    line3_onwards=$(tail -n +3 "$input")
    
    
    # Write to output file
    {   
        echo "#B3LYP/6-31+G(d) OPT FREQ"
        echo
        echo "$name"
        echo
        echo "0 1"
        echo "$line3_onwards"
        echo
    } > "$output"

    sed -i "1i\\
%nprocshared=32\\
%mem=8GB\\
%chk=$name.chk" "$output"

    sed -i "/OPT/c\\
#p PBEPBE/6-311+G**\\
opt freq\\
scf=(novaracc, tight)\\
int(grid=ultrafine)" "$output"
#scf=(xqc, maxcycle=200)

    echo "Saved to $output"
}

#xyz2_pbe_inp example_06_molecule.xyz example_06_molecule_pbe.com 

xyz2_lda_inp() {
    input="$1"
    output="$2"
    name="${3:-default}"

    if [[ ! -f "$input" ]]; then
        echo "Error: Input file '$input' not found."
        return 1
    fi

    # Read from line 3 to end
    line3_onwards=$(tail -n +3 "$input")


    # Write to output file
    {
        echo "#B3LYP/6-31+G(d) OPT FREQ"
        echo
        echo "$name"
        echo
        echo "0 1"
        echo "$line3_onwards"
        echo
    } > "$output"

    sed -i "1i\\
%nprocshared=32\\
%mem=8GB\\
%chk=$name.chk" "$output"

    sed -i "/OPT/c\\
#p LSDA/6-311G**\\
opt freq\\
scf=(novaracc, tight)\\
int(grid=ultrafine)" "$output"

    echo "Saved to $output"
}

#xyz2_lda_inp example_07_molecule.xyz example_07_molecule_lda.com 

### solvation effect  ###


xyz2_sol_inp() {
    input="$1"
    output="$2"
    func="$3"
    basis="$4"
    sol_val="$5"
    name="${6:-default}"

    if [[ ! -f "$input" ]]; then
        echo "Error: Input file '$input' not found."
        return 1
    fi

    # Read from line 3 to end
    line3_onwards=$(tail -n +3 "$input")


    # Write to output file
    {
        echo "#B3LYP/6-31+G(d) OPT FREQ"
        echo
        echo "$name"
        echo
        echo "0 1"
        echo "$line3_onwards"
        echo
	echo "Eps=$sol_val"
	echo
    } > "$output"

    sed -i "1i\\
%nprocshared=32\\
%mem=8GB\\
%chk=$name.chk" "$output"

    sed -i "/OPT/c\\
#p $func/$basis\\
opt freq\\
scf=(novaracc, tight)\\
int(grid=ultrafine)\\
SCRF(SMD, Read)" "$output"

    echo "Saved to $output"
}

#xyz2_sol_inp example_08_molecule.xyz example_08_molecule_pbe_sol.com PBEPBE 6-311+G** 3.1
#xyz2_sol_inp example_08_molecule.xyz example_08_molecule_hse_sol.com HSEh1PBE 6-311+G** 3.1


xyz2_gen_sol_inp() {
    input="$1"
    output="$2"
    func="$3"
    basis_path="$4"
    sol_val="$5"
    name="${6:-default}"

    if [[ ! -f "$input" ]]; then
        echo "Error: Input file '$input' not found."
        return 1
    fi

    # Read from line 3 to end
    line3_onwards=$(tail -n +3 "$input")
    
    
    # Write to output file

    # Write to output file
    {
        echo "#$func/gen OPT FREQ"
        echo "SCRF(SMD, Read)"
        echo
        echo "$name"
        echo
        echo "0 1"
        echo "$line3_onwards"
        echo
        echo "@$basis_path"
        echo
        echo "Eps=$sol_val"
        echo
    } > "$output"

    sed -i "1i\\
%nprocshared=32\\
%mem=64GB\\
%chk=$name.chk" "$output"

    echo "Saved to $output"
}

#basis_path="/mnt/home/k0122399/gauss/def2-QZVPD.bas"
#xyz2_sol_inp example_09_molecule.xyz example_09_molecule_pbe_sol.com PBEPBE 6-311+G** $basis_path 3.1
#xyz2_sol_inp example_09_molecule.xyz example_09_molecule_hse_sol.com HSEh1PBE 6-311+G** $basis_path 3.1



## similar to without solvents some specific functional and basis sets based function are defined for regular usage.

xyz2_b3lyp_sol_inp() {
    input="$1"
    output="$2"
    sol_val="$3"
    name="${4:-default}"

    if [[ ! -f "$input" ]]; then
        echo "Error: Input file '$input' not found."
        return 1
    fi

    # Read from line 3 to end
    line3_onwards=$(tail -n +3 "$input")


    # Write to output file
    {
        echo "#B3LYP/6-31+G(d) OPT FREQ"
        echo
        echo "$name"
        echo
        echo "0 1"
        echo "$line3_onwards"
        echo
    } > "$output"

    sed -i "1i\\
%nprocshared=32\\
%mem=8GB\\
%chk=$name.chk" "$output"

    sed -i "/OPT/c\\
#p B3LYP/6-311+G**\\
opt freq\\
scf=(novaracc, tight)\\
int(grid=ultrafine)\\
SCRF(SMD, Read)" "$output"

sed -i "\$a Eps=$sol_val \n" "$output"

    echo "Saved to $output"
}

#xyz2_b3lyp_sol_inp example_10_molecule.xyz example_10_molecule_b3lyp_sol.com 3.1


xyz2_hse_sol_inp() {
    input="$1"
    output="$2"
    sol_val="$3"
    name="${4:-default}"

    if [[ ! -f "$input" ]]; then
        echo "Error: Input file '$input' not found."
        return 1
    fi

    # Read from line 3 to end
    line3_onwards=$(tail -n +3 "$input")


    # Write to output file
    {
        echo "#B3LYP/6-31+G(d) OPT FREQ"
        echo
        echo "$name"
        echo
        echo "0 1"
        echo "$line3_onwards"
        echo
    } > "$output"

    sed -i "1i\\
%nprocshared=32\\
%mem=8GB\\
%chk=$name.chk" "$output"

    sed -i "/OPT/c\\
#p HSEh1PBE/6-311+G**\\
opt freq\\
scf=(novaracc, tight)\\
int(grid=ultrafine)\\
SCRF(SMD, Read)" "$output"

sed -i "\$a Eps=$sol_val \n" "$output"

    echo "Saved to $output"
}

#xyz2_hse_sol_inp example_11_molecule.xyz example_11_molecule_hse_sol.com 3.1

xyz2_pbe_sol_inp() {
    input="$1"
    output="$2"
    sol_val="$3"
    name="${4:-default}"

    if [[ ! -f "$input" ]]; then
        echo "Error: Input file '$input' not found."
        return 1
    fi

    # Read from line 3 to end
    line3_onwards=$(tail -n +3 "$input")


    # Write to output file
    {
        echo "#B3LYP/6-31+G(d) OPT FREQ"
        echo
        echo "$name"
        echo
        echo "0 1"
        echo "$line3_onwards"
        echo
    } > "$output"

    sed -i "1i\\
%nprocshared=32\\
%mem=8GB\\
%chk=$name.chk" "$output"

    sed -i "/OPT/c\\
#p PBEPBE/6-311+G**\\
opt freq\\
scf=(novaracc, tight)\\
int(grid=ultrafine)\\
SCRF(SMD, Read)" "$output"

sed -i "\$a Eps=$sol_val \n" "$output"

    echo "Saved to $output"
}

#xyz2_pbe_sol_inp example_12_molecule.xyz example_12_molecule_pbe_sol.com 3.1

xyz2_lda_sol_inp() {
    input="$1"
    output="$2"
    sol_val="$3"
    name="${4:-default}"

    if [[ ! -f "$input" ]]; then
        echo "Error: Input file '$input' not found."
        return 1
    fi

    # Read from line 3 to end
    line3_onwards=$(tail -n +3 "$input")


    # Write to output file
    {
        echo "#B3LYP/6-31+G(d) OPT FREQ"
        echo
        echo "$name"
        echo
        echo "0 1"
        echo "$line3_onwards"
        echo
    } > "$output"

    sed -i "1i\\
%nprocshared=32\\
%mem=8GB\\
%chk=$name.chk" "$output"

    sed -i "/OPT/c\\
#p LSDA/6-311+G**\\
opt freq\\
scf=(novaracc, tight)\\
int(grid=ultrafine)\\
SCRF(SMD, Read)" "$output"

sed -i "\$a Eps=$sol_val \n" "$output"

    echo "Saved to $output"
}


## getting optimized structure from output file and converting it to .xyz, which then can be converted to gaussian input file.

#xyz2_lda_sol_inp example_13_molecule.xyz example_13_molecule_lda_sol.com 3.1

get_opt_coords() {
    inp="$1"
    out="$2"
    awk -v fname="$inp" '
    /Standard orientation:/ {idx=NR} 
    END {
        cmd = "tail -n+" idx " " fname " | tail -n+6"
        while (cmd | getline line) {
            if (line ~ /^ ---/) break
            print line
        }
    }
    ' "$inp"  | awk '{printf "%-3s  %10.6f  %10.6f  %10.6f\n", $2, $4, $5, $6}' > $out
}

#get_opt_coords example_14_molecule.out  opt_coords.txt

opt_coords2xyz() {
    # Converting opt-structure into .xyz file
    input=$1
    output=$2
    declare -A elements=(
      [1]=H   [2]=He  [3]=Li  [4]=Be  [5]=B   [6]=C   [7]=N   [8]=O   [9]=F   [10]=Ne
      [11]=Na [12]=Mg [13]=Al [14]=Si [15]=P  [16]=S  [17]=Cl [18]=Ar [19]=K  [20]=Ca
      [21]=Sc [22]=Ti [23]=V  [24]=Cr [25]=Mn [26]=Fe [27]=Co [28]=Ni [29]=Cu [30]=Zn
      [31]=Ga [32]=Ge [33]=As [34]=Se [35]=Br [36]=Kr [37]=Rb [38]=Sr [39]=Y  [40]=Zr
      [41]=Nb [42]=Mo [43]=Tc [44]=Ru [45]=Rh [46]=Pd [47]=Ag [48]=Cd [49]=In [50]=Sn
      [51]=Sb [52]=Te [53]=I  [54]=Xe [55]=Cs [56]=Ba [57]=La [58]=Ce [59]=Pr [60]=Nd
      [61]=Pm [62]=Sm [63]=Eu [64]=Gd [65]=Tb [66]=Dy [67]=Ho [68]=Er [69]=Tm [70]=Yb
      [71]=Lu [72]=Hf [73]=Ta [74]=W  [75]=Re [76]=Os [77]=Ir [78]=Pt [79]=Au [80]=Hg
      [81]=Tl [82]=Pb [83]=Bi [84]=Po [85]=At [86]=Rn [87]=Fr [88]=Ra [89]=Ac [90]=Th
      [91]=Pa [92]=U  [93]=Np [94]=Pu [95]=Am [96]=Cm [97]=Bk [98]=Cf [99]=Es [100]=Fm
      [101]=Md [102]=No [103]=Lr [104]=Rf [105]=Db [106]=Sg [107]=Bh [108]=Hs [109]=Mt [110]=Ds
      [111]=Rg [112]=Cn [113]=Nh [114]=Fl [115]=Mc [116]=Lv [117]=Ts [118]=Og
    )
    
    n_atoms=$(wc -l < "$input")
    
    {
      echo "$n_atoms"
      echo "Optimized-structure"
      while read -r index x y z; do
        symbol=${elements[$index]}
        printf "%-2s %12.6f %12.6f %12.6f\n" "$symbol" "$x" "$y" "$z"
      done < "$input"
    } > "$output"

    echo "Saved to $output"
}

#opt_coords2xyz opt_coords.txt examples_15_opt.xyz


## getting status of the job.

get_status() {
    output=$1
    status_line=$(tail -n 1 "$output")

    # Check if the last line contains the exact phrase
    if echo "$status_line" | grep -q "Normal termination of Gaussian"; then
        echo "Status: $output : Completed"
        E0=$(grep "SCF Done" "$output" | awk '{print $5}' | tail -n 1)
        freq=$(grep "Frequencies --" "$output" | awk '{for(i=3;i<=NF;i++) printf "%s ", $i}')
        echo "E0: $E0"
        echo "Frequencies: $freq"
    else
        echo "Status: $output : Not-Completed"
        echo "E0: "
        echo "Frequencies: "
    fi
}

# getting status of a job examples_16_g16_ouput.out
#drct=$(pwd)
#get_status $drct/examples_16_g16_ouput.out

