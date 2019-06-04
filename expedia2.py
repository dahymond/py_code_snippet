for i in range(8):    
    link = 'https://www.expedia.com/'
    browser.get(link)
    time.sleep(5)
    #choose flights only
    flights_only = browser.find_element_by_xpath("//button[@id='tab-flight-tab-hp']")
    flights_only.click()
    ticket_chooser(return_ticket)
    dep_country_chooser('Cairo')
    arrival_country_chooser('New york')
    dep_date_chooser('04', '01', '2019')
    return_date_chooser('05', '02', '2019')
    search()
    compile_data()
    #save values for email
    current_values = df.iloc[0]
    cheapest_dep_time = current_values[0]
    cheapest_arrival_time = current_values[1]
    cheapest_airline = current_values[2]
    cheapest_duration = current_values[3]
    cheapest_stops = current_values[4]
    cheapest_price = current_values[-1]
    print('run {} completed!'.format(i))
    create_msg()
    connect_mail(username,password)
    send_email(msg)
    print('Email sent!')
    df.to_excel('flights.xlsx')
    time.sleep(3600)