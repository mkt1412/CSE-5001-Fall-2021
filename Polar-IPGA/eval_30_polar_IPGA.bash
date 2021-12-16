echo "Polar IPGA evaluation: $1"
for i in $(seq 1 1 30)
do
    echo $'\n'"Run time: $i" | tee -a $1_Polar_IPGA_log.txt
    python main.py -d $1 >> $1_Polar_IPGA_log.txt
done
echo "Done"