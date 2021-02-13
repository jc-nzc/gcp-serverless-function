

class Handler
  include Messaging::Handle
  include Messaging::StreamName

  dependency :write, Messaging::Postgres::Write
  dependency :clock, Clock::UTC
  dependency :store, Store

  def configure
    Messaging::Postgres::Write.configure(self)
    Clock::UTC.configure(self)
    Store.configure(self)
  end
