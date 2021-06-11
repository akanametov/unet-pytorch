import torch

#######################################################
#### Intersection Over Union (Jaccard Coefficient) ####
#######################################################

def IoUnion(preds, targets):
    
    intersection = (preds * targets).sum()
    union = preds.sum() + targets.sum() - intersection
    iou = torch.div(intersection, union)
    
    return iou

######################################################
############### Dice Coefficient #####################
######################################################

def DICE(preds, targets, smooth=1):
    
    intersection = (preds * targets).sum() + smooth
    union = preds.sum() + targets.sum() + smooth
    dice = torch.div(2*intersection, union)  

    return dice