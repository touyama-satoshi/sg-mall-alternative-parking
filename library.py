import requests

def carpark_lots(url,code): # the backend function used to find out how many available carpking lots, url is the API's url, code is the carpark code
    url10 = url
    response10 = requests.get(url10) #ping the API
    data10 = response10.json() #save data
    i_want = None #the carpark's details we want
    list_of_dict = data10["items"][0]["carpark_data"] # list of carparks (in the form of dict)
    for dictionary in list_of_dict:
        if dictionary.get("carpark_number") == code: #if the carpark_number corresonds to the carpark code we want
            i_want = dictionary #save it as i_want
            break
    available = i_want['carpark_info'][0]['lots_available'] #access variable that says lots available
    return available