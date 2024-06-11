require 'sinatra'
require 'json'
require 'logger'

class JsonLogger < Logger
  def format_message(severity, timestamp, progname, msg)
    JSON.dump({
      severity: severity,
      timestamp: timestamp,
      progname: progname,
      message: msg
    }) + "\n"
  end
end

log = JsonLogger.new(File.open("/var/log/ruby_app/app.log", "a"))

set :bind, '0.0.0.0'
set :port, 4567

get '/' do
  log.info("This is an info message")
  "Hello, world!"
end

get '/error' do
  log.error("This is an error message")
  "An error occurred!"
end
