
import math
import re



def format_desc_air(text):

    if "M1 " not in text and "M2 " not in text:
        return None
    

    pre_version = re.search(r"macbook\s+(air|pro)", text.lower(), re.IGNORECASE)
    if pre_version:
        m_version = pre_version.group(1).title()

    cpu_cores = None
    if m_version.lower() == 'air':
        cpu_regex = r"CPU .*?((Octa)?core|2core|4core)"
        cpu_match = re.search(cpu_regex, text)
        if cpu_match:
            cpu_str = cpu_match.group(1)
            if "Octa" in cpu_str:
                cpu_cores = 8
            elif "2core" in cpu_str:
                cpu_cores = 2
            elif "4core" in cpu_str:
                cpu_cores = 4
        else:
            cpu_cores = None
    else:
        cpu_regex = r"CPU .*?6+2|(\d+)core|(\d+)cores"
        cpu_match = re.search(cpu_regex, text)
        if cpu_match:
            cpu_str = cpu_match.group(1)
            # print([cpu_str])
            if '6+2' in cpu_str:
                cpu_cores=8
            else:
                cpu_cores = cpu_str
        else:
            cpu_cores = None
        # cpu_regex = re.compile(r"CPU.*?(\d+)core")
        # cpu_cores = cpu_regex.search(text)
        # if cpu_cores:
        #     cpu_cores = cpu_cores.group(1)
        # else:
        #     cpu_cores = "?"


    gpu_regex = re.compile(r"Graphics.*?(\d+)core")
    gpu_cores = gpu_regex.search(text)

    if gpu_cores:
        gpu_cores = gpu_cores.group(1)
    else:
        gpu_cores = "?"

    try:
        chip_version = re.search(r"(?<=M[12] )\w+", text).group(0).title()
        if 'pro' not in chip_version.lower() and 'max' not in chip_version.lower():
            chip_version = ''
        if 'pro' in chip_version.lower():
            chip_version = 'Pro'
        elif 'max' in chip_version.lower():
            chip_version = 'Max'
    except: 
        chip_version = ''

    c_match = re.search(r'Color\s+(\w+)', text)
    if c_match:
        color = c_match.group(1)

        if color == 'Gray':
            color = 'Space Gray'
        
    else:
        color = "?"


    chip_pattern = r"\bM[1-2]\b"

    chip_match = re.search(chip_pattern, text)

    if chip_match:
        chip = chip_match.group(0)
    else:
        chip = '?'

    

    pattern = r'(\d+\.\d+)\s*inches'

    r_match = re.search(pattern, text)

    if r_match:
        resolution = math.floor(float(r_match.group(1)))
        
    else:
        resolution = '?'
    
    if resolution < 14 and m_version == 'Pro':
        if chip == 'M1':
            cpu_cores = 8
            gpu_cores = 8
        elif chip == 'M2':
            cpu_cores = 8
            gpu_cores = 10

    return {'m_version': m_version, 'resolution': resolution, 'chip': chip, 'c_version': chip_version, 'cpu':cpu_cores, 'gpu': gpu_cores, 'color': color}

# print(format_desc_air('APPLE 2021 MacBook Pro 16 MK183KH A M1 ProNotebook Operating System OS macOS Monterey Screen Information 41.05cm 16.2 inches 3456x2234 1000nit Refresh Rate 120Hz CPU Apple ARM Silicon M1 PRO APL1103 10cores 8+2 RAM RAM Capacity 16GB RAM replacement Impossible Graphics Builtin graphics M1 PRO 16core storage SSD 512GB Network Wireless LAN 802.11ax WiFi 6 Video inputoutput HDMI Webcam FHD terminal Thunderbolt 4 3 USBC combined SD card Additional Features Fingerprint Recognition HighSpeed Charging USBPD DP Alt Mode Input Device Keyboard Light YType Direction Key Power Battery 100Wh Adapter 140W Charging Terminal MagSafe 3 Key Specifications Thickness 16.8mm Weight 2.1kg Cooling Fan 2 Color Gray 16core Neural Engine Up to 200GB s Memory Bandwidth Media Engine Decoding + Encoding + ProRes Notched Display Price KRW 3360000'))








'''
def format_desc_pro(text):


    cpu_regex = re.compile(r"CPU.*?(\d+)core")

    gpu_regex = re.compile(r"Graphics.*?(\d+)core")

    chip_version = re.search(r"(?<=M[12] )\w+", text).group(0)

    match = re.search(r'Color\s+(\w+)', text)
    
    chip_pattern = r"\bM[1-2]\b"

    chip_match = re.search(chip_pattern, text)

    if match:
        chip = chip_match.group(0)
    else:
        chip = '?'

    if match:
        color = match.group(1)
        if color == 'Gray':
            color = 'Space Gray'
        
    else:
        color = "?"

    pattern = r'(\d+\.\d+)\s*inches'

    match = re.search(pattern, text)

    if match:
        resolution = round(float(match.group(1)))
        
    else:
        resolution = '?'


    cpu_cores = cpu_regex.search(text)
    if cpu_cores:
        cpu_cores = cpu_cores.group(1)
    else:
        cpu_cores = "?"

    gpu_cores = gpu_regex.search(text)
    if gpu_cores:
        gpu_cores = gpu_cores.group(1)
    else:
        gpu_cores = "?"

    return {'resolution': resolution, 'chip': chip, 'c_version': chip_version, 'cpu':cpu_cores, 'gpu': gpu_cores, 'color': color}

'''



'''
####До изменений

def format_desc_air(text):

    if "M1 " not in text and "M2 " not in text:
        return None
    

    pre_version = re.search(r"macbook\s+(air|pro)", text.lower(), re.IGNORECASE)
    if pre_version:
        m_version = pre_version.group(1).title()

    cpu_cores = None
    if m_version.lower() == 'air':
        cpu_regex = r"CPU .*?((Octa)?core|2core|4core)"
        cpu_match = re.search(cpu_regex, text)
        if cpu_match:
            cpu_str = cpu_match.group(1)
            if "Octa" in cpu_str:
                cpu_cores = 8
            elif "2core" in cpu_str:
                cpu_cores = 2
            elif "4core" in cpu_str:
                cpu_cores = 4
        else:
            cpu_cores = None
    else:
        cpu_regex = re.compile(r"CPU.*?(\d+)core")
        cpu_cores = cpu_regex.search(text)
        if cpu_cores:
            cpu_cores = cpu_cores.group(1)
        else:
            cpu_cores = "?"


    gpu_regex = re.compile(r"Graphics.*?(\d+)core")
    gpu_cores = gpu_regex.search(text)

    if gpu_cores:
        gpu_cores = gpu_cores.group(1)
    else:
        gpu_cores = "?"

    try:
        chip_version = re.search(r"(?<=M[12] )\w+", text).group(0)
        if 'Pro' not in chip_version and 'Max' not in chip_version:
            chip_version = ''
    except: 
        chip_version = ''

    c_match = re.search(r'Color\s+(\w+)', text)
    if c_match:
        color = c_match.group(1)

        if color == 'Gray':
            color = 'Space Gray'
        
    else:
        color = "?"


    chip_pattern = r"\bM[1-2]\b"

    chip_match = re.search(chip_pattern, text)

    if chip_match:
        chip = chip_match.group(0)
    else:
        chip = '?'

    

    pattern = r'(\d+\.\d+)\s*inches'

    r_match = re.search(pattern, text)

    if r_match:
        resolution = math.floor(float(r_match.group(1)))
        
    else:
        resolution = '?'
    
    if resolution < 14 and m_version == 'Pro':
        if chip == 'M1':
            cpu_cores = 8
            gpu_cores = 8
        elif chip == 'M2':
            cpu_cores = 8
            gpu_cores = 10

    return {'m_version': m_version, 'resolution': resolution, 'chip': chip, 'c_version': chip_version, 'cpu':cpu_cores, 'gpu': gpu_cores, 'color': color}


'''