import os

test_path = "/home/alex/Documents/Clase/TFG/Dataset/iskra/"
test_filename = "1-2embarres.txt"
def open_doc(txt_path):
    """
    Opens a TXT document and returns its lines as a list.
    :param txt_path
    :return: list with the document lines.
    """
    with open(txt_path, encoding="ISO 8859-15") as txtFile:
        lines = txtFile.readlines()
    return lines

lines_list = open_doc(test_path + test_filename)


def get_tables_index(lines):
    """
        The files are in TXT form, and they have one table per sensor, with some
        text in between tables in between, so we need to know where each table
        starts and ends. Also, to seize the iteration of the file and with
        efficiency in mind, we also get the association between sensor codes
        and names.
        :param txt_path: Path to the TXT
        :return: List of pairs where the first element is the start index of the
        table, and the second is the end index, and a dictionary with the sensor
        code and its name.
    """

    line_counter = 0
    start_lines = []
    end_lines = []
    code_name_assoc = {}

    for line in lines:
        # Gets the association between sensor names and codes
        if "Transponder: " in line:
            code = line
            code = code.replace("Transponder: ", "")
            name = lines[line_counter + 1]
            if "Placement: " in name:
                name = name.replace("Placement: ", "")
                code_name_assoc[code] = name

        # Gets the starting index of the table
        if "Code" in line:
            start_lines.append(line_counter)

        # Gets the ending index candidates of the table, getting all the
        if line[0] == "\n":
            end_lines.append(line_counter)
        line_counter += 1
    # This line is needed because there is no \n in the end of the file,
    # and we need some way to indicate it
    end_lines.append(len(lines) - 1)

    start_end_index = []
    # Associates the start indices with its end indices
    for i in range(len(start_lines)):
        j = 0
        while start_lines[i] > end_lines[j] and j < len(end_lines) - 1:
            j += 1
        start_end_index.append([start_lines[i], end_lines[j]])
    return start_end_index, code_name_assoc


def get_sensors_list(lines):
    """
    Gets the tables for each sensor using the index ranges from get_tables_index
    function and returns a list with the sensor tables separated. These tables
    are in CSV format, so they are ready for exportation and Pandas library
    :param lines: the input file as a list type
    :return: List with the sensor tables
    """
    start_end_index, code_name = get_tables_index(lines)
    sensor_list = []
    for i in range(len(start_end_index)):
        sensor = []
        for j in range(start_end_index[i][0], start_end_index[i][1]):
            sensor.append(lines_list[j])
        sensor_list.append(sensor)
    return sensor_list



sensors = get_sensors_list(lines_list)

def list_to_csv(sensor_list):
    folder_name = test_filename.replace(".txt", "")
    if not os.path.exists(test_path + folder_name + "/"):
        os.mkdir(test_path + folder_name + "/")

    for i in range(len(sensor_list)):
        code = sensor_list[i][1].split(",")[0]
        with open(test_path + folder_name + "/" + code + ".csv", "w+") as csv:
            for row in sensors[i]:
                csv.write(row)
