import torch

print("torch version :", torch.__version__)
print("CUDA (torch)  :", torch.version.cuda)
print("is_available  :", torch.cuda.is_available())
assert torch.cuda.is_available(), "CUDA is NOT available to torch"

dev = torch.device("cuda")
print("device name   :", torch.cuda.get_device_name(0))
cc = torch.cuda.get_device_capability(0)
print("compute cap   : sm_%d%d" % cc)
print("arch list     :", torch.cuda.get_arch_list())

# Real kernel test: a matmul on the GPU. If sm_120 kernels are missing,
# this raises "CUDA error: no kernel image is available for execution".
a = torch.randn(4096, 4096, device=dev)
b = torch.randn(4096, 4096, device=dev)
c = a @ b
torch.cuda.synchronize()
print("matmul result : shape", tuple(c.shape), "device", c.device, "sum", float(c.sum()))
print("GPU SANITY CHECK PASSED")
