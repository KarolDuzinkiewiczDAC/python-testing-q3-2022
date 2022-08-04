import os
import yaml
import logging

class Class1:
    def __init__(self, config_filepath: str):
        '''
        Class constructor
        '''

        if not os.path.exists(config_filepath) or not os.path.isfile(config_filepath):
            raise ValueError('Invalid input argument \'config_filepath\'')

        # load configuration from YAML file
        with open(config_filepath) as f:
            self.config_dict = yaml.safe_load(f)
        logging.info(f'Loaded device config from: {config_filepath}')
        logging.debug(f'self.device_config_dict:\n{self.config_dict}')

        self.__verify_config()


    def __verify_config(self) -> bool:
        '''
        Verifies config file
        '''

        if 'param1' not in self.config_dict.keys() \
            or 'param2' not in self.config_dict.keys() \
            or 'param3' not in self.config_dict.keys():

            raise RuntimeError('Invalid config')


    def calculate_2nd_order_polynomial(self, x):
        '''
        Calculates 2nd order polynomial of x.

        Parameters:
            x

        Returns:
            value of polynomial
        '''

        return self.config_dict['param1'] * pow(x, 2) + self.config_dict['param2'] * x + self.config_dict['param3']
