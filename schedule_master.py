from matplotlib import pyplot as plt

class SheduleMaster():
    def __init__(self, data_file):
        self.data_file = data_file
        self.OFP = []



        self.read_data_file()
        self.OFP_plot()
        


    def read_data_file(self):
        with open(self.data_file, "r") as data_file:
            ofp_flag = False
            for row in data_file.readlines():
                if "/" in row and ofp_flag == True:
                    ofp_flag = False

                if ofp_flag == True:
                    self.OFP.append([float(i) for i in row.split()])
                    #print(row)
                if "SWOF" in row:
                    ofp_flag = True
    
    def OFP_plot(self):
        print(self.OFP)
        x = [row[0] for row in self.OFP]
        wather = [row[1] for row in self.OFP]
        oil = [row[2] for row in self.OFP]
        gas = [row[3] for row in self.OFP]

        plt.plot(x, wather, 'o-', color='blue', label='Проницаемость воды')
        plt.plot(x, oil, 'o-', color='red', label='Проницаемость нефти')
        plt.plot(x, gas, 'o-', color='green', label='Газонасыщенность')
        plt.show()
                    


if __name__ == "__main__":
    data_file_path = input()
    sm = SheduleMaster(data_file_path)
