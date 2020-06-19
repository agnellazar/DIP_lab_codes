clc;clear;close all;
% Agnel Lazar Alappat

% Order
N = 10;

% Low pass filter
h_lp = 1/N.*ones(1,N);
% High pass filter
h_hp = [h_lp(1:length(h_lp)/2).*(-1) h_lp(length(h_lp)/2+1:end).*(1)];
I = imread('lena2.png');
I_gray = rgb2gray(I);

% Filtering
I_filter_lp = conv2(I_gray,h_lp,'same');
I_filter_hp = conv2(I_gray,h_hp,'same');

% Showing images
figure;
subplot(1,3,1)
imshow(I_gray);
title('Original')
subplot(1,3,2)
imshow(mat2gray(I_filter_lp));
title('Lowpass Filtered')
subplot(1,3,3)
imshow(mat2gray(I_filter_hp));
title('Highpass Filtered')