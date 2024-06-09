"""
i have 3 table post tags posttags i want 
and i have post-id  i want to get all recommended posts that share common tags e
xcluding the post-id and order them by the number of common tags
"""
@post_id :=1
select p2.id,p2.title,p2.content,
count(pt2.tag_id) as common_tags_count

from postags pt1
join posttags pt2 
on  pt1.tag_id=pt2.tag_id and pt1.post_id!=pt2.post_id
join posts p2 on pt2.post_id=p2.id
where pt1.id= @post_id
group by pt2.post_id,p2.title,p2.content
order by common_tags_count desc

