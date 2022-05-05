from datetime import datetime, date


def save_log(file, output, data):

    with open(file, 'a') as file:
        file.write('\n')
        file.write('Date: ')
        file.write(datetime.now().strftime("%H:%M:%S"))
        file.write(' ')
        file.write(str(date.today()))
        file.write(" Output: " + str(output))

        file.write(data)
        file.write('\n')