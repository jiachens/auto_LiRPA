###
 # @Description: 
 # @Autor: Jiachen Sun
 # @Date: 2022-01-27 17:00:00
 # @LastEditors: Jiachen Sun
 # @LastEditTime: 2022-01-28 17:18:03
### 

for model in 'resnet18_b256_CROWN-IBP_epoch2000_start=101,length=801,mid=0.4_0.25'; do

mkdir ./output/${model}

for cor in 'contrast' 'fog' 'gaussian_noise' 'shot_noise' 'impulse_noise' 'defocus_blur' 'frosted_glass_blur' 'motion_blur' 'zoom_blur' 'snow' 'frost' 'brightness' 'elastic' 'pixelate' 'jpeg_compression'; do
for sev in 1 2 3 4 5; do

CUDA_VISIBLE_DEVICES=0 python ./cifar_training.py --verify --model ${model} --load pretrain/Densenet_cifar --norm 2 --eps 0.25 --data CIFAR-C  --corruption ${cor} --severity ${sev} > ./output/${model}/${cor}_${sev}.out

done
done
done