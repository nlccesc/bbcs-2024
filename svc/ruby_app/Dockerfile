FROM ruby:2.7

WORKDIR /app

COPY Gemfile Gemfile.lock ./

RUN bundle install

COPY . .

CMD ["rackup", "--host", "0.0.0.0", "--port", "4567"]
