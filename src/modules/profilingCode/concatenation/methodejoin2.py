# -*- coding: utf-8 -*-
import sys
import src.modules.utils.logger as utils

__all__ = ['methodejoin2']


def methodejoin2(n):
    """
    Function methodejoin2 which allow to concatenate the character string 'Name' n times more faster than methodejoin1.

    Exception management :
    If any exception : log the trace of the exception stack and stop the execution of the programme

    :param n: Integer indicating the number of times the concatenation will be performed
    :type n: integer
    :return: The character string resulting from the concatenation of n times 'Name'
    :rtype: str
    """
    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Start of function methodejoin2, input n (number of occurrences) = %s', str(n))

    try:
        result = []
        try:
            for i in range(n):
                result.append('Name')
            return ''.join(result)
        except Exception as e:
            logger.error('Exception : problem during methodejoin2 = %s', str(n))
            sys.exit()
    except Exception as e:
        logger.error('Exception : problem during methodejoin2 = %s', str(n))
        sys.exit()