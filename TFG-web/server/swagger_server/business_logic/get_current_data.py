from swagger_server.DAO.towdataDAO import TowdataDAO


class GetCurrentData:

    def get_current_data(self, limit):
        df = TowdataDAO.getData(TowdataDAO)

        try:
            data = df.drop(columns=["Tiempo", "Escalas(m)"])
        except:
            data = df.drop(columns=["Tiempo", "Datos1(Fa)"])
        json_format = []
        i = 0
        for index, row in data.iterrows():
            escalas = row["Datos1(m)"]
            json_format.append([i, escalas])
            i += 1
        if len(json_format) - limit > 0:
            response = json_format[len(json_format) - limit:]
        else:
            response = json_format
        return response
