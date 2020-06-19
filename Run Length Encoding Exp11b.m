clc;clear;close all;
%Agnel Lazar Alappat

% Generating Random binary values...
x = round(rand(1,100));

% RLE
A = RLE1_SGD(x);

% Converting to binary
B = reshape(A,[2,length(A)/2]);
Bit_stream = [];
m = ceil(log2(max(B(2,:))));

% Converting to binary
for ii = 1:length(A)/2
    n = B(2,ii);
    BitStream = Dec2Bin_SGD(n,m);
    Bit_stream = [Bit_stream [BitStream B(1,ii)];];
end

CR = length(Bit_stream)./length(x);
if CR<1
    disp(['Compression Factor: ' num2str(CR)]);
else
    disp('Negative Compression!!!!');
end