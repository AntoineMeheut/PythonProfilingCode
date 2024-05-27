# -*- coding: utf-8 -*-
import sys
import src.modules.utils.logger as utils

__all__ = ['methodejoin1']


def methodejoin1(n):
    """
    Function methodejoin1 which allow to concatenate the character string 'Name' n times.

    Exception management :
    If any exception : log the trace of the exception stack and stop the execution of the programme

    :param n: Integer indicating the number of times the concatenation will be performed
    :type n: integer
    :return: The character string resulting from the concatenation of n times 'Name'
    :rtype: str
    """
    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Start of function methodejoin1, input n (number of occurrences) = %s', str(n))

    try:
        result = ''
        try:
            for i in range(n):
                result += 'Name'
            return result
        except Exception as e:
            logger.error('Exception : problem during methodejoin1 = %s', str(n))
            sys.exit()
    except Exception as e:
        logger.error('Exception : problem during methodejoin1 = %s', str(n))
        sys.exit()
