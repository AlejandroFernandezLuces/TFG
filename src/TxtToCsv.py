import os


class FileManaging:
    def __init__(self, filepath, filename):
        """
        Encapsulates everything related to plain text to CSV files.
        :param filepath:
        :param filename:
        """
        self._filepath = filepath
        self._filename = filename
        self._lines = self._open_doc(filepath + filename)
        self._sensor_list = self._get_sensors_list()

    def _open_doc(self, file):
        """
        Opens a TXT document and returns its lines as a list.
        :param file
        :return: list with the document lines.
        """
        with open(file, encoding="ISO 8859-15") as txtFile:
            lines = txtFile.readlines()
        return lines

    def _get_tables_index(self):
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

        for line in self._lines:
            # Gets the association between sensor names and codes
            if "Transponder: " in line:
                code = line
                code = code.replace("Transponder: ", "")
                name = self._lines[line_counter + 1]
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
        end_lines.append(len(self._lines) - 1)

        start_end_index = []
        # Associates the start indices with its end indices
        for i in range(len(start_lines)):
            j = 0
            while start_lines[i] > end_lines[j] and j < len(end_lines) - 1:
                j += 1
            start_end_index.append([start_lines[i], end_lines[j]])
        return start_end_index, code_name_assoc
        # TODO: substituir codigos por nomes

    def _get_sensors_list(self):
        """
        Gets the tables for each sensor using the index ranges from
        get_tables_index function and returns a list with the sensor tables
        separated. These tables are in CSV format, so they are ready for
        exportation and Pandas library
        :param lines: the input file as a list type
        :return: List with the sensor tables
        """
        start_end_index, code_name = self._get_tables_index()
        sensor_list = []
        for i in range(len(start_end_index)):
            sensor = []
            for j in range(start_end_index[i][0], start_end_index[i][1]):
                sensor.append(self._lines[j])
            sensor_list.append(sensor)
        return sensor_list

    def list_to_csv(self):
        """
        Gets a csv for every sensor in the sensor list
        :param sensor_list: A list of lists where each element is a CSV table for
        each sensor. We need it this way to access each row separately.
        :param filename: The name of the original file, because we need to create a
        folder to keep all CSVs from a file together.
        :param filepath: Path to the file.
        :return: Creates the CSV and saves them in the indicated path
        """
        new_filename = self._filename.replace(".txt", "")
        if not os.path.exists(self._filepath + new_filename + "/"):
            os.mkdir(self._filepath + new_filename + "/")

        for i in range(len(self._sensor_list)):
            code = self._sensor_list[i][1].split(",")[0]
            with open(self._filepath + new_filename + "/" + code + ".csv", "w+") as csv:
                for row in self._sensor_list[i]:
                    csv.write(row)

