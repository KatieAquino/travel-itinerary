const Route = ReactRouterDOM.Route;
const Link = ReactRouterDOM.Link;
const Switch = ReactRouterDOM.Switch;
const Router = ReactRouterDOM.BrowserRouter;

const Homepage = (props) => {
  return (
    <div>
      <h1>Welcome</h1>
      <h2>Plan Your Next Adventure</h2>
        <Login/>
        <NewUser/>
    </div>
  );
}

const Login = (props) => {
  return (
    <section>
      Returning User
    </section>
  );
}

const NewUser = (props) => {
  return (
    <section>
      New User
    </section>
  );
}

const TravelApp = (props) => {
  
  return (
    <Router>
      <div>
        <nav>
          <Link to="/">Home</Link>
        </nav>
        
        <Switch>
          <Route path="/">
            <Homepage />
          </Route>
        </Switch>

      </div>
    </Router>
  );
}

ReactDOM.render(
  <TravelApp />,
  document.querySelector('#root')
);