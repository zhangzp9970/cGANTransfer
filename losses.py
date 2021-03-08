import torch
import torch.nn.functional as F

# DCGAN loss
def loss_dcgan_dis(dis_fake, dis_real):
  L1 = torch.mean(F.softplus(-dis_real))
  L2 = torch.mean(F.softplus(dis_fake))
  return L1, L2


def loss_dcgan_gen(dis_fake):
  loss = torch.mean(F.softplus(-dis_fake))
  return loss


# Hinge Loss
def loss_hinge_dis(dis_fake, dis_real):
  loss_real = torch.mean(F.relu(1. - dis_real))
  loss_fake = torch.mean(F.relu(1. + dis_fake))
  return loss_real, loss_fake



def loss_hinge_gen(dis_fake, comb_params=None, res_params=None, comb_l1_scale=0, res_l2_scale=0):
  loss = -torch.mean(dis_fake)

  # l1 regularization over similarity scores
  if comb_params != None:
    for p in comb_params:
      loss += comb_l1_scale * torch.mean(torch.abs(p))

  # l2 regularization over BN residual parameters
  if res_params != None:
    for p in res_params:
      loss += res_l2_scale * torch.mean(p**2)
  return loss



# Default to hinge loss
generator_loss = loss_hinge_gen
discriminator_loss = loss_hinge_dis
