############################################################
#
#    main.py
#
############################################################

import smtplib
server = smtplib.SMTP('smtp.keme.net')

server.sendmail('seddon-software@keme.co.uk', 'seddon-software@keme.co.uk', \
"""To: abc-software@keme.co.uk
From: seddon-software@keme.co.uk
Beware the Ides of March.
""") 

server.quit()

1

