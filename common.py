from decimal import Decimal as D

__all__ = ["D", "dec", "say", "BTC_PREC", "USD_PREC"]

BTC_PREC = D('0.00000001')
USD_PREC = D('0.00001')

# talking
def say(text):
  print text
  #festival = subprocess.os.popen2("echo '(SayText \"" + text.replace("'", "") + "\")' | /usr/bin/festival --pipe")

# align D number at decimal point
def dec(dec, before, after):
  rc = ''
  if dec.as_tuple().exponent >= 0:
    rc = "%i.0" % int(dec)
    rc = "%*s" % (before+1-len(rc), rc)
  else:
    rc = str(dec.normalize())
  #print dec, rc
  if rc.find('.') >= 0:
    rc = "%*s" % (before-rc.find('.')+len(rc), rc)
  rc += '                          '[:(after+before+1)-len(rc)]
  rc = rc[:(before+after+1)]
  return rc # rc.replace('0.', 'o.').replace('.0', '.o')