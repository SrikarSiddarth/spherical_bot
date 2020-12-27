add the following text to the gazebo.material file present at 'usr/share/gazebo-7/media/materials/scripts/':

material Gazebo/CustomTransparent
{
  technique
  {
    pass
    {
      scene_blend alpha_blend
      depth_write off

      ambient 1.0 1.0 0.0 0.1
      diffuse 1.0 1.0 0.0 0.1

      texture_unit
      {
        colour_op_ex source1 src_current src_current 0 1 0
        alpha_op_ex source1 src_manual src_current 0.1
      }
    }
  }
}