# -*- coding: utf-8 -*-
import sys
import src.modules.utils.logger as utils

__all__ = ['methodejoin3']


def methodejoin3(n):
    """
    Function methodejoin3 which allow to calculate the first n rows of the multiplication table by 10.

    Exception management :
    If any exception : log the trace of the exception stack and stop the execution of the programme

    :param n: Integer indicating the number of times the concatenation will be performed
    :type n: integer
    :return: The character string resulting from the concatenation of n times 'Name'
    :rtype: str
    """
    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Start of function methodejoin3, input n (number of occurrences) = %s', str(n))

    try:
        result = ''
        try:
            for i in range(n):
                result += str(i) + ' x 10 = ' + str(i * 10) + ' ; '
            return result
        except Exception as e:
            logger.error('Exception : problem during methodejoin3 = %s', str(n))
            sys.exit()
    except Exception as e:
        logger.error('Exception : problem during methodejoin3 = %s', str(n))
        sys.exit()
