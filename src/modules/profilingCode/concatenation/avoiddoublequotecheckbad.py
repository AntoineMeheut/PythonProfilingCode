# -*- coding: utf-8 -*-
import sys
import src.modules.utils.logger as utils

__all__ = ['avoiddoublequotecheckbad']


def avoiddoublequotecheckbad(n):
    """
    Function avoiddoublequotecheckbad which allow to concatenate the character string 'Name' n times.

    Exception management :
    If any exception : log the trace of the exception stack and stop the execution of the programme

    :param n: Integer indicating the number of times the concatenation will be performed
    :type n: integer
    :return: The character string resulting from the concatenation of n times 'Renault', 'Fiat', 'Citroen'
    :rtype: str
    """
    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Start of function avoiddoublequotecheckbad, input n (number of occurrences) = %s', str(n))

    try:
        result = []
        try:
            for var in [var2 for var2 in range(n)]:
                result += ["Renault", "Fiat", "Citroen"]
            return result
        except Exception as e:
            logger.error('Exception : problem during avoiddoublequotecheckbad = %s', str(n))
            sys.exit()
    except Exception as e:
        logger.error('Exception : problem during avoiddoublequotecheckbad = %s', str(n))
        sys.exit()

