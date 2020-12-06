import torch.nn as nn
from torch.nn.modules.loss import _Loss
from catalyst.contrib.nn.criterion.focal import FocalLossMultiClass

class Loss:
  def __init__(self, loss_name, switch = 3):

    self.counter = 0
    self.switch = switch
    self.loss_name = loss_name
    self.loss = {
        'ce': nn.CrossEntropyLoss(),
        'bce': nn.BCELossWithLogits(),
        'focal': FocalLossMultiClass()
    }

  def __call__(self, pred, target, epoch=0):
    loss = self.loss[self.loss_name]
    if epoch > self.switch:
      loss = self.loss['focal']
      
    self.counter += 1
    return loss(pred, target)