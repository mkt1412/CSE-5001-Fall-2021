echo "Baseline evaluation: $1"
for i in $(seq 1 1 30)
do
    echo $'\n'"Run time: $i" | tee -a $1_baseline_log.txt
    python main.py -d $1 >> $1_baseline_log.txt
done
echo "Done"