% MatLab Code for applying LPF and HPF on an image.
% Written by Agnel Lazar Alappat BT17ECE003
clc;clear;close all; N = 10; % Order of Filter
% Low pass filter 
h_lp = 1/N.*ones(1,N); % High pass filter
h_hp = [h_lp(1:length(h_lp)/2).*(-1) h_lp(length(h_lp)/2+1:end).*(1)];
I = imread('fruits.jpg');
I_gray = rgb2gray(I);
% Filtering
I_filter_lp = conv2(I_gray,h_lp,'same');
I_filter_hp = conv2(I_gray,h_hp,'same');
% Showing images 
figure; subplot(1,3,1) 
imshow(I_gray); 
title('Original Image') 
subplot(1,3,2) 
imshow(mat2gray(I_filter_lp)); 
title('Low Pass Filtered') 
subplot(1,3,3) 
imshow(mat2gray(I_filter_hp)); 
title('High Pass Filtered')
