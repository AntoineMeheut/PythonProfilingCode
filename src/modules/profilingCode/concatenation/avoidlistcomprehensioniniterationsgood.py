# -*- coding: utf-8 -*-
import sys
import src.modules.utils.logger as utils

__all__ = ['avoidlistcomprehensioniniterationsgood']


def avoidlistcomprehensioniniterationsgood(n: object) -> object:
    """
    Function avoidlistcomprehensioniniterationsgood

    Exception management :
    If any exception : log the trace of the exception stack and stop the execution of the programme

    :param n: Integer indicating the number of times the concatenation will be performed
    :type n: integer
    :return: The character string resulting from the concatenation of n times 'Name'
    :rtype: str
    """
    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Start of function avoidlistcomprehensioniniterationsgood, input n (number of occurrences) = %s', str(n))

    try:
        result = ''
        try:
            for var in (var2 for var2 in range(n)):
                result += 'Name'
            return result
        except Exception as e:
            logger.error('Exception : problem during avoidlistcomprehensioniniterationsgood = %s', str(n))
            sys.exit()
    except Exception as e:
        logger.error('Exception : problem during avoidlistcomprehensioniniterationsgood = %s', str(n))
        sys.exit()
