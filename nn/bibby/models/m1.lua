-- baseline model
-- https://github.com/htwaijry/npy4th
npy4th = require 'npy4th'
require 'image'
require 'nn'



-- builder the model
model = nn.Sequential()
--nn.SpatialConvolution(nInputPlane, nOutputPlane, kW, kH, [dW], [dH], [padW], [padW])
model:add(nn.SpatialConvolution(3,32, 3,3, 1,1, 0,0))
model:add(nn.ReLU())
model:add(nn.SpatialConvolution(32,32, 3,3, 1,1, 0,0))
model:add(nn.ReLU())
model:add(nn.SpatialMaxPooling(2,2))

model:add(nn.SpatialConvolution(32,64, 3,3, 1,1, 0,0))
model:add(nn.ReLU())
model:add(nn.SpatialConvolution(64,64, 3,3, 1,1, 0,0))
model:add(nn.ReLU())
model:add(nn.SpatialMaxPooling(2,2))

-- flatten the matrix, find the compenents by taking the size of the matrices after the last pooling
model:add(nn.View(64*5*3)) 

-- build a classifier
classifer = nn.Sequential()
classifer:add(nn.Linear(64*5*3, 600))
classifer:add(nn.ReLU())
classifer:add(nn.Linear(600,2))
-- classifer:add(nn.LogSoftMax())
-- -- add the classifier to the model
model:add(classifer)

return model