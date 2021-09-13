root_dir=$1
size=$2
cd $root_dir
count=0
for subd in */; do
	count=$((count+1))
done
index=0
for subd in */; do
	index=$((index+1))
	echo $index"/"$count
	cd $subd
	mkdir render/
	for f in *.obj; do
		pref=`echo $f | cut -d'.' -f1`
		RenderShape -u y -v 00- -z 1 $f "./render/"$pref".jpg" $size $size
	done
	cd ..
done
