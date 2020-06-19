clc;clear;close all;
% Agnel Lazar Alappat

Img = imread('lena.jpeg');
Img_gray = rgb2gray(Img);

[cA1,cH1,cV1,cD1] = dwt2(Img_gray,'haar');
Img_edge = mat2gray(cD1);

figure;
subplot(1,2,1)
imshow(Img_gray)
subplot(1,2,2)
imshow(Img_edge)