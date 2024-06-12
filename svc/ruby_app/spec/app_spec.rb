require_relative '../app'
require 'rspec'
require 'rack/test'

ENV['RACK_ENV'] = 'test'

RSpec.describe 'The Ruby App' do
  include Rack::Test::Methods

  def app
    Sinatra::Application
  end

  it "says hello" do
    get '/'
    expect(last_response).to be_ok
    expect(last_response.headers['Content-Type']).to include('text/html')
    expect(last_response.body).to eq('Hello, world!')
  end

  it "logs an error and returns the appropriate message" do
    get '/error'
    expect(last_response).to be_ok
    expect(last_response.headers['Content-Type']).to include('text/html')
    expect(last_response.body).to eq('An error occurred!')
  end

  it "returns a 404 for unknown routes" do
    get '/unknown'
    expect(last_response.status).to eq(404)
    expect(last_response.headers['Content-Type']).to include('text/html')
    response = last_response.body
    expect(response).to include('Sinatra doesn’t know this ditty.')
  end

  it "returns appropriate headers for security" do
    get '/'
    expect(last_response).to be_ok
    expect(last_response.headers['X-Frame-Options']).to eq('DENY')
    expect(last_response.headers['X-Content-Type-Options']).to eq('nosniff')
    expect(last_response.headers['X-XSS-Protection']).to eq('1; mode=block')
  end
end
