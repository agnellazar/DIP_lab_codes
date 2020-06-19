clc;clear;close all;
% Written by Agnel Lazar Alappat
min_slope = 5;
max_slope = 255;

Img = imread('lena.jpeg');
Img_gray = rgb2gray(I);

[r c] = size(Img_gray);                       % Size of gray image
len = row * col;                                % Total number of pixels
Img_vec = Img_gray(:);                              % Vectorinzing the matrix
Img_sort = sort(Img_vec);                           % Sorting the values in ascending values
Img_unq = unique(Img_sort);                         % Finding unique values

Img_min = min(Img_unq);
Img_max = max(Img_unq);

% Slope
Slope = (max_slope-min_slope)./(Img_max-Img_min);
new_slope = Slope.*(Img_unq-Img_min)+min_slope;

% Stretching
Img_stretched = zeros(r,c);
for jj = 1:length(Img_unq)
    Img_str(Img_gray == Img_unq(jj)) = new_slope(jj);
end

Img_str = uint8(I_str);
figure;
subplot(2,2,1)
imshow(Img_gray)
title('Original')
subplot(2,2,2)
imshow(Img_str)
title('Stretched')
subplot(2,2,3)
histogram(Img_gray)
subplot(2,2,4)
histogram(Img_str)


