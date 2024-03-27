import os
import re
import urllib.parse
import urllib.request

def download_files(first_url, output_dir):
    #  check to see if the requested output directory exists and if don't, create it.
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    #  break the input URL into the head and tail.
    url_head, url_tail = os.path.split(first_url)
    #  use the regular expression findall function on tail to identify the last group of digits
    first_index = re.findall(r'[0-9]+', url_tail)[-1]

    index_count, error_count = 0, 0
    while error_count < 5:
        # the next index value is the sum of the first_index plus the index_count value
        next_index = str(int(first_index) + index_count)
        # if the first_index is zero padded, append the number of zeroes to the front of the next_index string
        if first_index[0] == '0':
            next_index = '0' * (len(first_index) - len(next_index)) + next_index
        #  use urljoin() to combine the orifinal URL head and a modified URL tail with the next_index value
        next_url = urllib.parse.urljoin(url_head, re.sub(first_index, next_index, url_tail))

        try:
            #  generate the file path for where to save the file
            output_file = os.path.join(output_dir, os.path.basename(next_url))
            #  download and save
            urllib.request.urlretrieve(next_url, output_file)
            print(f'Successfully downloaded {os.path.basename(next_url)}')
        except IOError:
            print(f'Could not retrieve {next_url}')
            error_count += 1
        index_count += 1


download_files('http://699340.youcanlearnit.net/image001.jpg', 'images')
