import { useEffect, useState } from "react";
import ArticleItem from "./ArticleItem";

function Home(props) {

  const {API_URL,user}=props
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    fetch(`${API_URL}/articles`,{
      credentials: "include",
    })
      .then((r) => r.json())
      .then(setArticles);
  }, []);

  const isUser=user ? (
    <h1>Welcome, {user.username}!</h1>
    ):(<h1>Please Login or Sign Up</h1>)

  return (
    <main>
      {isUser}
      {articles.map((article) => (
        <ArticleItem key={article.id} article={article} />
      ))}
    </main>
  );
}

export default Home;