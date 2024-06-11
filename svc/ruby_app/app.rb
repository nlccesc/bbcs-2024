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


log_directory = ENV['RACK_ENV'] == 'test' ? './logs' : './logs'

Dir.mkdir(log_directory) unless File.exist?(log_directory)

log = JsonLogger.new(File.open("#{log_directory}/app.log", "a"))

set :bind, '0.0.0.0'
set :port, 4567


get '/' do
  log.info("This is an info statement")
  "Hello, world!"
end

get '/error' do
  log.error("This is an error statement")
  "An error occurred!"
end
