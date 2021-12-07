from glob import glob
import os
import click


"""
批量修改文件名
两处需要修改
"""    
# First position to modify
tar_dir = '/Users/king/Downloads/tmp'
file_list = glob(os.path.join(tar_dir, '*.mp4'))


confirm_flag = True
processed_cnt = 0
for i, file_path in enumerate(file_list):
    file_name = os.path.basename(file_path)
    
    # Second position to modify
    new_name = file_name[3:]
    
    
    new_path = os.path.join(tar_dir, new_name)
    action_flag = True
    if confirm_flag:
        if click.confirm(f'{file_name} -> {new_name}?'):
            # os.rename(file_path, new_path)
            action_flag = True
            if click.confirm(f'Apply to all?'):
                confirm_flag = False
        else:
            action_flag = False
    if action_flag:
        os.rename(file_path, new_path)
        processed_cnt += 1


print(f'Processed {processed_cnt}/{len(file_list)} files')