""" This file was written by Suan Ali and Libaan Olow, this code generates a queue of customers, while each customer is
generated the customers is assigned to a lane based of their items in their basket
"""

import random  # imports random module so that random functions can be used
import time  # the time module is imported for the purpose of the simulation where customers are generated
# between the number of seconds stated
from datetime import datetime


class Customer:

    def __init__(self, number):
        self.number = number
        self.__items = random.randint(0, 30)  # private member/attribute

    # __init__ is a constructor when creating object/attributes of a class
    # number is used to identify the customer
    # random function is used to generate a number between 0 and 30
    # random number generated is the number of items that the customer will have in their basket


class Basket(Customer):
    """ This class generates important details of a customer that include items in their basket, whether they won a
    lottery or not, and the till processing times
    """
    cashier_till = 4  # class variable > cashier till is a constant
    self_service = 6  # class variable > self-service is also a constant

    # These 2 are constants because they are fixed processing times

    def __init__(self, number):
        super().__init__(number)
        self.__items = None

    def basket(self):
        self.__items = random.randint(0, 30)  # randomly generates a number of items between 0 and 30
        return self.__items  # random number generated is saved into the instance variable 'items'

    def lottery(self):
        if self.__items > 9:
            return "yes".upper()
        else:
            return "no".upper()

    # lottery function is used to verify if the number generated is greater than 9
    # if yes then customer wins a lottery ticket
    # if items is less than 9 then customer doesn't win a lottery ticket

    def cashier(self):  # abstract method overridden
        ct = self.__items * Basket.cashier_till
        return ct

    def ss_till(self):  # abstract method overridden
        st = self.__items * Basket.self_service
        return st


# constants (fixed variables) include cashier till and self_service
# the processing time will be calculated by using the number of items generated and the constant
# The processing time is items generated * constant (cashier till)


items_lottery = Basket(None)

# the purpose of the Checkout class is to display the details of the customer
# the details include:
# identifier of the customer
# items in the customers basket
# if the customer won a lottery ticket or not
# the time to process the basket which depends on the number of items and which lane the customer is in


hour = time.strftime('%H:%M:%S')


class Lane:
    now = datetime.now()
    timestamp = datetime.timestamp(now)

    def __init__(self, lane_type, status, timestamp=timestamp):
        self.lane_type = lane_type
        self.status = status
        self.timestamp = timestamp

    def initial_choose_lane(self):
        # lane options
        self.lane_type = ["Self-Service", "Regular"]
        # indication statement that simulation has begun, and the timestamp next to it
        print("Simulation Begin:", hour)


lane = Lane("Regular", "Open")


class Checkout(Basket):

    def __init__(self, number, item, lottery, cashier, ss):  # instance variables
        super().__init__(number)
        self.number = number
        self.cashier = cashier
        self.item = item
        self.lottery = lottery
        self.ss = ss


# the super function helps with not having to write the code of the parent class again
# the above instance variables


def display(number):
    items_1 = items_lottery.basket()
    lottery = items_lottery.lottery()
    times = items_lottery.cashier()
    self_service = items_lottery.ss_till()
    return Checkout(number, items_1, lottery, times, self_service)


# the purpose of the Checkout class is to display the details of the customer
# the details include:
# identifier of the customer
# items in the customers basket
# if the customer won a lottery ticket or not
# the time to process the basket which depends on the number of items and which lane the customer is in


def generation(maximum=0):
    """ this function generates a queue of customers which are assigned to a specific lane
    """
    num_of_customers = []  # this variable is a list of customers
    counter = 0
    self_service_count2 = 0
    regular_count2 = 0
    remove_regular = 0
    print("Regular Lane:", "Open")
    print("Regular Lane:", "Closed")
    print("Regular Lane:", "Closed")
    print("Regular Lane:", "Closed")
    print("Regular Lane:", "Closed""\n")

    print("Self-service Lane:", "Open")
    print("Customers in Queue:", "\n")
    while maximum == 0 or counter < maximum:  # while loop will only execute if the user says 'Yes' to the prompt
        counter += 1  # increments by 1 for every loop
        customer = display(counter)  # 'customer' is equal to the function 'display' which contains customer details
        num_of_customers.append(customer)  # the 'customer' variable output is moved to the 'num_of_customers' list
        if customer.lottery == "YES":
            print("### Lucky Customer ###")
        else:
            print("### Customer details ### ")
        print("Customer", customer.number, "->", "items in basket:", customer.item, "\n""Lottery Winner?", end="")
        print("", customer.lottery, "\ncashier till processing time:", customer.cashier, "sec")
        print("self-service processing time:", customer.ss, "sec", "\n")
        time.sleep(2)
        if customer.item < 10:
            self_service_count2 += 1
            print(f"Customer {customer.number} joined Self-Service Lane", "checked out in: ", end="")
            print(items_lottery.ss_till(), "secs""\n")
        if customer.item > 10:
            regular_count2 += 1
            print(f"Customer {customer.number} joined Regular Lane", "checked out in: ", end="")
            print(items_lottery.cashier(), "secs""\n")
        if customer.item > 10 and regular_count2 == 5:
            remove_regular = regular_count2 - 5
            regular_count2 = 5
        if customer.item > 10 and regular_count2 > 5:
            remove_regular += 1
        time.sleep(2)  # a customer is generated every 2 seconds
    print(f"Number of customers moved: {remove_regular}")
    print("Customers in self service lane:", self_service_count2)
    print("Customers in regular lane:", regular_count2)
    prompt = input("Continue Simulation?""\n")  # asks the user if they want to continue the simulation
    if prompt == "Yes":
        generation(simulation)
    return num_of_customers  # this return statement will return/output when the 'generation' function is run


simulation = random.randint(0, 10)  # the simulation will generate random number of customers between 0 and 10


class Result:
    def output(self):
        """ outputs the generation and lane_initial_choose_lane functions in the console
        """
        lane.initial_choose_lane()
        generation(simulation)


console = Result()
console.output()
