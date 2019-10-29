import os


class FileManager:
    def __init__(self, dataset_path):
        """
        Encapsulates everything related to the conversion of
         plain text files to CSV files, and the selection of these plain
         text files. We must initialize the instance with the path of the
         dataset
        :param dataset_path: path to the location of the dataset
        :param filename: name of the concrete file to convert
        """
        self._dataset_path = dataset_path

    def _open_doc(self, file):
        """
        Opens a TXT document and returns its lines as a list.
        :param file
        :return: list with the document lines.
        """
        absolute_path = self._dataset_path + "/" + file
        with open(absolute_path, encoding="ISO 8859-15") as txtFile:
            lines = txtFile.readlines()
        return lines

    def _get_tables_index(self, lines):
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
                code = code.replace("\n", "")
                name = lines[line_counter + 1]
                if "Placement: " in name:
                    name = name.replace("Placement: ", "")
                    name = name.replace("\n", "")
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

    def _get_sensors_list(self, lines):
        """
        Gets the tables for each sensor using the index ranges from
        get_tables_index function and returns a list with the sensor tables
        separated. These tables are in CSV format, so they are ready for
        exportation and Pandas library
        :param lines: the input file as a list type
        :return: List with the sensor tables
        """
        start_end_index, code_name = self._get_tables_index(lines)
        sensor_list = []
        column_num = 9 # NUMERO HARD CODED!!
        for i in range(len(start_end_index)):
            sensor = []
            sensor_code = lines[start_end_index[i][0] + 1].split(",")[0]
            # TODO: deshardcodear o numero de columnas
            #column_num = len(lines[start_end_index[i][0] + 1].split(","))
            for j in range(start_end_index[i][0], start_end_index[i][1]):
                line = lines[j]
                splitted_line = line.split(",")
                if len(splitted_line) > 9:
                    splitted_line = splitted_line[:column_num - 1]
                    splitted_line.append("\n")
                line = ",".join(splitted_line)
                sensor_name = code_name[sensor_code]
                line = line.replace(sensor_code, sensor_name)
                sensor.append(line)

            sensor_list.append(sensor)
        return sensor_list

    def _rename_sensor(self, code, line, dict):
        """
        Substitutes the code name (i.e. C59D) to a human readable name.
        :param code:
        :param line:
        :param dict:
        :return:
        """
        name = dict[code]
        return line.replace(code, name)

    def get_csv(self, filename):
        """
        Gets a csv for every sensor in the sensor list
        :param sensor_list: A list of lists where each element is a CSV table for
        each sensor. We need it this way to access each row separately.
        :param filename: The name of the original file, because we need to create a
        folder to keep all CSVs from a file together.
        :param filepath: Path to the file.
        :return: Creates the CSV and saves them in the indicated path
        """
        new_filename = filename.replace(".txt", "") # Name of the new folder
        absolute_path = self._dataset_path + "/" + new_filename + "/"

        if not os.path.exists(absolute_path):
            os.mkdir(absolute_path)
        lines = FileManager._open_doc(self, filename)
        sensor_list = FileManager._get_sensors_list(self, lines)
        for i in range(len(sensor_list)):
            code = sensor_list[i][1].split(",")[0]
            with open(absolute_path + code + ".csv", "w+") as csv:
                for row in sensor_list[i]:
                    csv.write(row)

    def get_all_csv(self):
        """
        Iterates all TXT files in the specified directory and converts them
        to the appropiate CSV files, using the get_csv function
        :return:
        """
        filenames = os.listdir(self._dataset_path)
        for filename in filenames:
            if ".txt" in filename:
                FileManager(self._dataset_path).get_csv(filename)