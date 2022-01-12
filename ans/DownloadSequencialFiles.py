import os
import re
import urllib.parse
import urllib.request

def save_response(fp, response):
    """https://www.linkedin.com/learning/python-code-challenges/download-sequential-files"""
    block_size = 1024
    while True:
        try:
            block = response.read(block_size)
            if not block:
                break
            fp.write(block)
        except:
            raise

def download_files(url, output_dir_path):
    
    if not os.path.isdir(s=output_dir_path):
        os.mkdir(output_dir_path)
    url_head, url_tail = os.path.split(url)
    first_index = re.findall(r'[0-9]+', url_tail)[-1] # + is greedy
    index_count, error_count = 0, 0
    while (error_count < 5):
        next_index = str(int(first_index) + index_count)
        if first_index[0] == '0':
            next_index = '0' * (len(first_index) - len(next_index)) + next_index

        pattern_repl_instr = re.sub(first_index, next_index, url_tail)
        next_url = urllib.parse.urljoin(url_head, pattern_repl_instr)

        final_str_component = os.path.basename(next_url)
        output_file_name = os.path.join(output_dir_path, final_str_component)

        try:
            with urllib.request.urlopen(url=url) as response, open(output_file_name, "xb") as fp:
                url = next_url
                print(f"{output_file_name} downloaded successfully!")
                save_response(fp, response)
        except BaseException as e:
            error = {str(e) : e}
            print(f'Error due to: {error}')
            error_count += 1
        index_count += 1

def main(url='http://699340.youcanlearnit.net/image001.jpg', output_dir_path='DownloadSequencialFiles_images'):
    download_files(url, output_dir_path)
    # http://699340.youcanlearnit.net/image051.jpg

if __name__ == '__main__':
    main()
