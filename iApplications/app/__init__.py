# # app.py

# from werkzeug.middleware.dispatcher import DispatcherMiddleware # use to combine each Flask app into a larger one that is dispatched based on prefix

# from iCore import app as Core
# from iWork import app as Work

# application = DispatcherMiddleware(Core, {
#     '/iwork':Work
# })

# # application = iCore
from iWork import app as Work

application = Work
