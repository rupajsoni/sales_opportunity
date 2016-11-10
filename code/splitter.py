import sys

def lexis_nexis_splitter(input_filename, max):
	input_file = open(input_filename)
	output_file_path = "/".join(input_filename.split("/")[:-1])
	output_file_path += "/output"
	output_file_suffix = "_" + input_filename.split("/")[-1]
	output_file = None
	
	for line in input_file :
		if " of " + str(max) + " DOCUMENTS" in line :
			doc_number = line.split(" of " + str(max) + " DOCUMENTS")[0].strip()
			output_file = open(output_file_path + "/" + doc_number + output_file_suffix, "w")
		if output_file is not None:
			output_file.write(line + "\n")
	
if __name__ == "__main__" :
	if sys.argv[2] == "ln" :
		lexis_nexis_splitter(sys.argv[1], sys.argv[3])