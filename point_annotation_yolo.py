
!pip install ultralytics==8.0.20
import ultralytics
ultralytics.checks()

from ultralytics import YOLO
from IPython import display

from IPython.display import display,Image



!pip install ultralytics

from google.colab import drive
drive.mount('/content/drive')



ls

from ultralytics import YOLO

model = YOLO('yolov8l-pose.pt')

data_path = '/content/drive/MyDrive/data.yml'
epochs = 300
batch_size = 8
learning_rate = 0.001
momentum = 0.9
weight_decay = 0.0005
optimizer = 'adam'
scheduler = 'cosine'

# Train the model with defined hyperparameters
model.train(data=data_path,
            epochs=epochs,
            batch_size=batch_size,
            lr=learning_rate,
            momentum=momentum,
            weight_decay=weight_decay,
            optimizer=optimizer,
            scheduler=scheduler,
            warmup_epochs=warmup_epochs)

model.train(data='/content/drive/MyDrive/data.yml',epochs = 300)


!yolo task = detect mode = train model = yolov8s.pt data=data.yaml epochs = 75 plots = True
