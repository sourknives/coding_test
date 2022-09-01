"""Contentful Senior Security Engineer Coding Test - September 2022"""
from jsonplaceholder import JsonPlaceholder


def main():
    """Main function that collects evidence to satisfy all Success Criteria"""
    # Initialize JsonPlaceholder Client
    jp = JsonPlaceholder()

    """
    Success Criteria #1: Retrieve all posts
        a.	Turn the JSON formatted text string returned that contains all posts into a list
        b.	Print out the total number of posts returned
    """
    # Instantiate an empty list to dump all posts into
    all_posts = []
    # Run GET request for all posts
    sc_1 = jp.get("posts")
    # Iterate through all posts and append to result_list
    for post in sc_1:
        all_posts.append(post)
    post_count = len(all_posts)
    print(f"SC1:\nThere are {post_count} posts in total.\n\n")

    """
    Success Criteria #2: Retrieve post #10
        a.	Print the title of post #10
        b.	Print the value of the “encoding” property returned in the object
        c.	In the headers property returned in the object, print the value of the ‘X-Powered-By’ Key
    """
    # GET request for post 10. return_type set to full in order to collect other properties
    sc_2 = jp.get("posts", resource_number=10, return_type="full")
    encoding = sc_2.encoding
    x_powered_header = sc_2.headers.get('X-Powered-By')
    # JSON-ify the response and get the title
    title = sc_2.json().get('title')
    print(f"SC2:\nPost 10 title: {title}\nEncoded property: "
          f"{encoding}\nX-Powered-By: {x_powered_header}\n\n")

    """
    Success Criteria #3: Retrieve all posts from User ID 7
        a.	Print the number of posts associated with this user
    """
    user_seven_posts = []
    sc_3 = jp.get("posts")
    for post in sc_3:
        if post.get('userId') == 7:
            user_seven_posts.append(post)
        seven_count = len(user_seven_posts)
    print(f"SC3:\nUser ID 7 has made {seven_count} posts.\n\n")

    """
    Success Criteria #4: Get all comments from Post 8
        a.	Turn the JSON formatted text string returned that contains all posts into a list
        b.	For each list item:
            i.	swap the value for ‘name’ and ‘email’
            ii.	Turn the list object back into a JSON formatted text string
            iii.	Print the new JSON formatted text string
            iv.	Using the PUT method, update each comment with the new swapped values
            v.	If the PUT is successful, print the text field of the return object
    """
    print("SC4:")
    # Instantiate empty list for comments
    post_eight_comments = []
    # Using the full resource route to get only comments for post 8
    sc_4 = jp.get(resource="posts/8/comments")
    # Add all post 8 comments to a list
    for comment in sc_4:
        post_eight_comments.append(comment)
    # Iterate through comment list to swap name and email values and PUT updated comments
    for comment in post_eight_comments:
        comment['name'], comment['email'] = comment['email'], comment['name']
        # **This may be an error** PUT request only returns 200 at post/# level
        put_req = jp.put(resource="posts/8/comments", data=str(comment))
        # This may be a product of the PUT request only working at post level. All ids return as 8
        print(f"PUT request for comment {comment.get('id')}: {put_req.get('id')}")
    # Convert object back to a JSON formatted text string and print
    comments_to_string = str(post_eight_comments)
    print(f"\nComments back to JSON formatted string:\n{comments_to_string}\n\n")

    """
    # Success Criteria #5: Attempt to get post 101.  Print the title of the post if successful.
    """
    # GET request for post 101, which will raise a 404
    sc_5 = jp.get("posts", resource_number=101, return_type="full")
    print(f"SC5:\nResponse code for Post #101 - {sc_5.status_code}\n\n")

    print("Done.")


if __name__ == "__main__":
    main()
