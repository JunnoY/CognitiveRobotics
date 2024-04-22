import numpy as np
import matplotlib.pyplot as plt

epoch_list = np.arange(1, 51, 1)
testing_loss_list_all_128 = np.load("./testing_losses_128.npy")
testing_accuracy_list_all_128 = np.load("./testing_accuries_128.npy")
testing_loss_list_all_256 = np.load("./testing_losses_256.npy")
testing_accuracy_list_all_256 = np.load("./testing_accuries_256.npy")
testing_accuracy_list_all_512 = np.load("./testing_accuries_512.npy")
testing_loss_list_all_512 = np.load("./testing_losses_512.npy")
testing_accuracy_list_all_1024 = np.load("./testing_accuries(1024).npy")
testing_loss_list_all_1024 = np.load("./testing_losses(1024).npy")



plt.figure(figsize=(8,6))
plt.plot(epoch_list, testing_loss_list_all_128[0], label='bs = 128, lr=0.001, wd=0.0001')
plt.plot(epoch_list, testing_loss_list_all_128[1], label='bs = 128, lr=0.001, wd=0.001')
plt.plot(epoch_list, testing_loss_list_all_128[2], label='bs = 128, lr=0.001, wd=0.01')
plt.plot(epoch_list, testing_loss_list_all_128[3], label='bs = 128, lr=0.01, wd=0.0001')
# plt.plot(epoch_list, testing_loss_list_all_128[4], label='bs = 128, lr=0.01, wd=0.001')
# plt.plot(epoch_list, testing_loss_list_all_128[5], label='bs = 128, lr=0.01, wd=0.01')
plt.plot(epoch_list, testing_loss_list_all_128[6], label='bs = 128, lr=0.1, wd=0.0001')
# plt.plot(epoch_list, testing_loss_list_all_128[7], label='bs = 128, lr=0.1, wd=0.001')
# plt.plot(epoch_list, testing_loss_list_all_128[8], label='bs = 128, lr=0.1, wd=0.01')
plt.plot(epoch_list, testing_loss_list_all_256[0], label='bs = 256, lr=0.001, wd=0.0001')
# plt.plot(epoch_list, testing_loss_list_all_256[1], label='bs = 256, lr=0.001, wd=0.001')
# plt.plot(epoch_list, testing_loss_list_all_256[2], label='bs = 256, lr=0.001, wd=0.01')
# plt.plot(epoch_list, testing_loss_list_all_256[3], label='bs = 256, lr=0.01, wd=0.0001')
# plt.plot(epoch_list, testing_loss_list_all_256[4], label='bs = 256, lr=0.01, wd=0.001')
# plt.plot(epoch_list, testing_loss_list_all_256[5], label='bs = 256, lr=0.01, wd=0.01')
# plt.plot(epoch_list, testing_loss_list_all_256[6], label='bs = 256, lr=0.1, wd=0.0001')
# plt.plot(epoch_list, testing_loss_list_all_256[7], label='bs = 256, lr=0.1, wd=0.001')
# plt.plot(epoch_list, testing_loss_list_all_256[8], label='bs = 256, lr=0.1, wd=0.01')
plt.plot(epoch_list, testing_loss_list_all_512[0], label='bs = 512, lr=0.001, wd=0.0001')
# plt.plot(epoch_list, testing_loss_list_all_512[1], label='bs = 512, lr=0.001, wd=0.001')
# plt.plot(epoch_list, testing_loss_list_all_512[2], label='bs = 512, lr=0.001, wd=0.01')
plt.plot(epoch_list, testing_loss_list_all_512[3], label='bs = 512, lr=0.01, wd=0.0001')
# plt.plot(epoch_list, testing_loss_list_all_512[4], label='bs = 512, lr=0.01, wd=0.001')
# plt.plot(epoch_list, testing_loss_list_all_512[5], label='bs = 512, lr=0.01, wd=0.01')
# plt.plot(epoch_list, testing_loss_list_all_512[6], label='bs = 512, lr=0.1, wd=0.0001')
# plt.plot(epoch_list, testing_loss_list_all_512[7], label='bs = 512, lr=0.1, wd=0.001')
# plt.plot(epoch_list, testing_loss_list_all_512[8], label='bs = 512, lr=0.1, wd=0.01')
# plt.plot(epoch_list, testing_loss_list_all_1024[0], label='bs = 1024, lr=0.001, wd=0.0001')
# plt.plot(epoch_list, testing_loss_list_all_1024[1], label='lr=0.001, wd=0.001')
# plt.plot(epoch_list, testing_loss_list_all_1024[2], label='lr=0.001, wd=0.01')
# plt.plot(epoch_list, testing_loss_list_all_1024[3], label='lr=0.01, wd=0.0001')
# plt.plot(epoch_list, testing_loss_list_all_1024[4], label='lr=0.01, wd=0.001')
# plt.plot(epoch_list, testing_loss_list_all_1024[5], label='lr=0.01, wd=0.01')
# plt.plot(epoch_list, testing_loss_list_all_1024[6], label='lr=0.1, wd=0.0001')
# plt.plot(epoch_list, testing_loss_list_all_1024[7], label='lr=0.1, wd=0.001')
# plt.plot(epoch_list, testing_loss_list_all_1024[8], label='lr=0.1, wd=0.01')

title = "Validation loss with changing batch size, learning rate and weight decay"
plt.title(title)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.savefig(f"./{title}.png", dpi=300)


plt.figure(figsize=(8,6))
plt.plot(epoch_list, testing_accuracy_list_all_128[0], label='bs = 128, lr=0.001, wd=0.0001')
plt.plot(epoch_list, testing_accuracy_list_all_128[1], label='bs = 128, lr=0.001, wd=0.001')
plt.plot(epoch_list, testing_accuracy_list_all_128[2], label='bs = 128, lr=0.001, wd=0.01')
plt.plot(epoch_list, testing_accuracy_list_all_128[3], label='bs = 128, lr=0.01, wd=0.0001')
# plt.plot(epoch_list, testing_accuracy_list_all_128[4], label='bs = 128, lr=0.01, wd=0.001')
# plt.plot(epoch_list, testing_accuracy_list_all_128[5], label='bs = 128, lr=0.01, wd=0.01')
plt.plot(epoch_list, testing_accuracy_list_all_128[6], label='bs = 128, lr=0.1, wd=0.0001')
# plt.plot(epoch_list, testing_accuracy_list_all_128[7], label='bs = 128, lr=0.1, wd=0.001')
# plt.plot(epoch_list, testing_accuracy_list_all_128[8], label='bs = 128, lr=0.1, wd=0.01')
plt.plot(epoch_list, testing_accuracy_list_all_256[0], label='bs = 256, lr=0.001, wd=0.0001')
# plt.plot(epoch_list, testing_accuracy_list_all_256[1], label='bs = 256, lr=0.001, wd=0.001')
# plt.plot(epoch_list, testing_accuracy_list_all_256[2], label='bs = 256, lr=0.001, wd=0.01')
# plt.plot(epoch_list, testing_accuracy_list_all_256[3], label='bs = 256, lr=0.01, wd=0.0001')
# plt.plot(epoch_list, testing_accuracy_list_all_256[4], label='bs = 256, lr=0.01, wd=0.001')
# plt.plot(epoch_list, testing_accuracy_list_all_256[5], label='bs = 256, lr=0.01, wd=0.01')
# plt.plot(epoch_list, testing_accuracy_list_all_256[6], label='bs = 256, lr=0.1, wd=0.0001')
# plt.plot(epoch_list, testing_accuracy_list_all_256[7], label='bs = 256, lr=0.1, wd=0.001')
# plt.plot(epoch_list, testing_accuracy_list_all_256[8], label='bs = 256, lr=0.1, wd=0.01')
plt.plot(epoch_list, testing_accuracy_list_all_512[0], label='bs = 512, lr=0.001, wd=0.0001')
# plt.plot(epoch_list, testing_accuracy_list_all_512[1], label='bs = 512, lr=0.001, wd=0.001')
# plt.plot(epoch_list, testing_accuracy_list_all_512[2], label='bs = 512, lr=0.001, wd=0.01')
plt.plot(epoch_list, testing_accuracy_list_all_512[3], label='bs = 512, lr=0.01, wd=0.0001')
# plt.plot(epoch_list, testing_accuracy_list_all_512[4], label='bs = 512, lr=0.01, wd=0.001')
# plt.plot(epoch_list, testing_accuracy_list_all_512[5], label='bs = 512, lr=0.01, wd=0.01')
# plt.plot(epoch_list, testing_accuracy_list_all_512[6], label='bs = 512, lr=0.1, wd=0.0001')
# plt.plot(epoch_list, testing_accuracy_list_all_512[7], label='bs = 512, lr=0.1, wd=0.001')
# plt.plot(epoch_list, testing_accuracy_list_all_512[8], label='bs = 512, lr=0.1, wd=0.01')
# plt.plot(epoch_list, testing_accuracy_list_all_1024[0], label='bs = 1024, lr=0.001, wd=0.0001')
# plt.plot(epoch_list, testing_accuracy_list_all_1024[1], label='lr=0.001, wd=0.001')
# plt.plot(epoch_list, testing_accuracy_list_all_1024[2], label='lr=0.001, wd=0.01')
# plt.plot(epoch_list, testing_accuracy_list_all_1024[3], label='lr=0.01, wd=0.0001')
# plt.plot(epoch_list, testing_accuracy_list_all_1024[4], label='lr=0.01, wd=0.001')
# plt.plot(epoch_list, testing_accuracy_list_all_1024[5], label='lr=0.01, wd=0.01')
# plt.plot(epoch_list, testing_accuracy_list_all_1024[6], label='lr=0.1, wd=0.0001')
# plt.plot(epoch_list, testing_accuracy_list_all_1024[7], label='lr=0.1, wd=0.001')
# plt.plot(epoch_list, testing_accuracy_list_all_1024[8], label='lr=0.1, wd=0.01')

title = "Validation accuracy with changing batch size, learning rate and weight decay"
plt.title(title)
plt.xlabel('Epoch')
plt.ylabel('Accuracy (%)')
plt.legend()
plt.savefig(f"./{title}.png", dpi=300)