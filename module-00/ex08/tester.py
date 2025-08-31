from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(100)):
    sleep(0.005)
    
ft_tqdm(range(100))
print()

